def palindromes_between_indices(s: str) -> set:
    palindromes = set()
    english_letters = ''.join(filter(str.isalpha, s[3:6].lower()))
    for i in range(len(english_letters)):
        for j in range(i + 3, len(english_letters) + 1):
            palindrome = english_letters[i:j]
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes