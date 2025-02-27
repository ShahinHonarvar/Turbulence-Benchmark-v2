from collections import defaultdict

def palindromes_between_indices(s):
    if len(s) < 10:
        return set()

    def is_palindrome(s):
        return s == s[::-1]

    def generate_palindromes(s):
        d = defaultdict(list)
        for i in range(len(s)):
            d[s[i]].append(i)
        result = set()
        for k, v in d.items():
            for i in range(len(v) - 2):
                for j in range(i + 2, len(v)):
                    if is_palindrome(s[v[i]:v[j] + 1]):
                        result.add(s[v[i]:v[j] + 1])
        return result
    return generate_palindromes(''.join(s[7:10]).lower())