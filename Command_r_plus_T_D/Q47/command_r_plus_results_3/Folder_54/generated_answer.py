def palindromes_of_specific_lengths(s: str) -> set:
    palindromes = set()
    substring = s[26:78].lower()
    for i in range(len(substring) - 17):
        for j in range(2):
            possible_palindrome = substring[i:i + 18 + j]
            if possible_palindrome == possible_palindrome[::-1] and possible_palindrome.isalpha():
                palindromes.add(possible_palindrome)
    return palindromes