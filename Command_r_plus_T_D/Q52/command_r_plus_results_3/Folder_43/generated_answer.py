def palindrome_of_length_n(s: str) -> set:

    def is_palindrome(sub_s: str) -> bool:
        return sub_s.lower() == sub_s.lower()[::-1]
    palindromes = set()
    str_length = len(s)
    for i in range(str_length - 50):
        for j in range(i + 1, str_length - i):
            sub_s = s[i:j]
            if len(sub_s) == 51 and all((c.isalpha() for c in sub_s)) and is_palindrome(sub_s):
                palindromes.add(sub_s)
    return palindromes