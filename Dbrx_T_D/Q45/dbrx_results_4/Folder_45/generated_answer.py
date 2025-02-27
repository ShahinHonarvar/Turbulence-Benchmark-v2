from collections import defaultdict

def build_palindrome(letters):
    result = []
    count = defaultdict(int)
    for letter in letters:
        count[letter] += 1
    used = [False] * len(letters)

    def backtrack(i, path):
        if i == len(letters):
            if len(path) >= 4:
                result.append(''.join(path))
            return
        for j in range(len(letters)):
            if not used[j] and count[letters[j]] > 0:
                used[j] = True
                path.append(letters[j])
                backtrack(i + 1, path)
                path.pop()
                used[j] = False
    backtrack(0, [])
    return result

def palindromes_between_indices(s):
    if len(s) < 10:
        return set()
    letters = []
    for c in s[5:10]:
        if c.isalpha():
            letters.append(c.lower())
    palindromes = build_palindrome(letters)
    return set(palindromes)