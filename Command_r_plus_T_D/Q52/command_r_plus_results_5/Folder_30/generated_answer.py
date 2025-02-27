def palindrome_of_length_n(s: str) -> set:

    def is_palindrome(sub_s: str) -> bool:
        return sub_s.lower() == sub_s.lower()[::-1]
    palindromes = set()
    length = len(s)
    for i in range(length):
        for j in range(i + 1, length + 1):
            sub_s = s[i:j]
            if len(sub_s) == 94 and all((char.isalpha() for char in sub_s)) and is_palindrome(sub_s):
                palindromes.add(sub_s)
    return palindromes