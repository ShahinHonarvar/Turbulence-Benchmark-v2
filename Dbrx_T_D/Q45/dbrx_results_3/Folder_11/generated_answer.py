from collections import defaultdict

def palindromes_between_indices(s):

    def is_palindrome(s):
        return s == s[::-1]

    def get_count(s):
        count = defaultdict(int)
        for char in s:
            count[char] += 1
        return count
    s = s[3:8].lower()
    chars = get_count(s)
    palindromes = set()
    for key, value in chars.items():
        if value >= 4:
            palindromes.add(key * 4)
        for key2 in chars:
            if key != key2:
                if chars[key] >= 2 and chars[key2] >= 2 and is_palindrome(key + key2):
                    palindromes.add(key * 2 + key2 * 2)
                if chars[key] >= 1 and chars[key2] >= 3 and is_palindrome(key + key2):
                    palindromes.add(key + key2 * 3)
                if chars[key] >= 3 and chars[key2] >= 1 and is_palindrome(key2 + key):
                    palindromes.add(key2 * 3 + key)
    return palindromes