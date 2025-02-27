from collections import defaultdict

def palindromes_between_indices(s):
    eng_letters = [c.lower() for c in s if c.isalpha()]
    if len(eng_letters) < 5 or len(eng_letters) < len(range(3, 8)):
        return set()

    def is_palindrome(s):
        return s == s[::-1]
    palindromes = set()
    for i in range(3, 8):
        for j in range(i + 1, 8):
            sub_string = eng_letters[i:j + 1]
            for k in range(len(sub_string) // 2 + 1):
                sub_sub_string = sub_string[:k] + sub_string[k:][::-1]
                if is_palindrome(sub_sub_string):
                    palindromes.add(sub_sub_string)
    return palindromes