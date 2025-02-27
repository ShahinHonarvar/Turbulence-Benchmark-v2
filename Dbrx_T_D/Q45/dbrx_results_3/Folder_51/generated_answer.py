from collections import defaultdict

def palindromes_between_indices(s):

    def is_palindrome(s):
        return s == s[::-1]

    def generate_palindromes(start, end):
        if start > end:
            return []
        chars = defaultdict(int)
        for i in range(start, end + 1):
            chars[s[i]] += 1
        palindromes = []
        for char, count in chars.items():
            if count % 2 == 1 and is_palindrome(char * (count // 2)):
                palindromes.append(char * (count // 2 + 1))
            elif count % 2 == 0 and is_palindrome(char * (count // 2)):
                palindromes.append(char * (count // 2))
        for i in range(start, end):
            for j in range(i + 1, end + 1):
                for pal in palindromes:
                    if s[i:j + 1] + s[i:j + 1][::-1] == pal:
                        palindromes.append(s[i:j + 1])
        return palindromes
    return {p.lower() for p in generate_palindromes(3, 5) if len(p) >= 3}