from collections import Counter
    from math import factorial

def palindrome_of_length_at_least_n(s):

    def get_all_substrings(s):
        n = len(s)
        return [s[i:j] for i in range(n) for j in range(i + 1, n + 1)]

    def check_palindrome(s):
        return s == s[::-1] and len(s) >= 31
    palindromes = set()
    s = s.lower()
    counter = Counter(s)
    for v in counter.values():
        for i in range(v, 0, -1):
            for c in counter.keys():
                counter.update(c * i)
            for substring in get_all_substrings(''.join(counter.elements())):
                if check_palindrome(substring):
                    palindromes.add(substring)
        counter = Counter(s)
    return palindromes