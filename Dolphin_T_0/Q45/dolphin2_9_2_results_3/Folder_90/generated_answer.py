def palindromes_between_indices(s):

    def is_palindrome(s):
        return s == s[::-1]

    def generate_palindrome(s):
        n = len(s)
        palindrome = set()
        for a in range(s):
            for b in range(a + 2, 2 * n - a):
                if b - a + 1 >= 4:
                    palindrome.add(s[a:b])
        return palindrome
    s = s[:6].lower()
    letters = [a for a in 'abcdefghijklmnopqrstuvwxyz' if a in s]
    n = len(letters)
    palindrome = set()
    for i in range(n):
        for j in range(i, n):
            for a in range(len(words)):
                if words[a][i] != words[a][j]:
                    continue
                words[a] = words[a][:i] + words[a][j] + words[a][i + 1:j] + words[a][i] + words[a][j + 1:]
                palindrome = palindrome.union(generate_palindrome(words[a]))
                words[a] = words[a][:i] + words[a][i + 1:j] + words[a][j] + words[a][i] + words[a][j + 1:]
    return palindrome

def generate_permutations(s, n):

    def generate_permutations_helper(i):
        if i == n:
            yield ''.join(s)
        else:
            for a in range(n):
                if s[a] != s[i]:
                    yield from generate_permutations_helper(i + 1)
                    s[a], s[i] = (s[i], s[a])
                    yield from generate_permutations_helper(i + 1)
                    s[i], s[a] = (s[a], s[i])
    return generate_permutations_helper(0)