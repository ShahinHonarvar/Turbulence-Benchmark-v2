def palindromes_of_specific_lengths(s: str) -> set:
    palindromes = set()
    substring = s[26:78].lower()
    for i in range(len(substring) - 17):
        for j in range(2):
            current_palindrome = substring[i:i + 18 + j]
            if current_palindrome == current_palindrome[::-1] and current_palindrome.isalpha():
                palindromes.add(current_palindrome)
    return palindromes