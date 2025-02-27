import re

def palindromes_of_specific_lengths(s: str) -> set:

    def is_palindrome(sub: str) -> bool:
        return sub == sub[::-1]
    sub_string = s[26:85]
    palindromes = set()
    cleaned_sub = re.sub('[^a-zA-Z]', '', sub_string).lower()
    for length in range(30, 47):
        for start in range(len(cleaned_sub) - length + 1):
            candidate = cleaned_sub[start:start + length]
            if is_palindrome(candidate):
                palindromes.add(candidate)
    return palindromes