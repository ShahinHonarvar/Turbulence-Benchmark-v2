def palindromes_between_indices(s: str) -> set:

    def is_palindrome(s):
        return s == s[::-1]
    palindromes = set()
    for i in range(1, 5):
        substring = s[i].lower()
        if substring.isalpha():
            for j in range(i + 1, 5):
                another_substring = s[j].lower()
                if another_substring.isalpha():
                    two_char_palindrome = substring + another_substring
                    if is_palindrome(two_char_palindrome):
                        palindromes.add(two_char_palindrome)
                    if j + 1 < 5:
                        yet_another_substring = s[j + 1].lower()
                        if yet_another_substring.isalpha():
                            three_char_palindrome = substring + another_substring + yet_another_substring
                            if is_palindrome(three_char_palindrome):
                                palindromes.add(three_char_palindrome)
    return palindromes