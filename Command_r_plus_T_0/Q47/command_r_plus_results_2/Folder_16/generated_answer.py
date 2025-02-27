def palindromes_of_specific_lengths(s: str) -> set[str]:
    palindromes = set()
    substring = s[14:87].lower()
    for i in range(len(substring) - 50):
        for length in range(51, 61):
            if length + i > len(substring):
                break
            temp_palindrome = substring[i:i + length]
            if temp_palindrome == temp_palindrome[::-1] and temp_palindrome.isalpha():
                palindromes.add(temp_palindrome)
    return palindromes