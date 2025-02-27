def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]

    def generate_permutations(chars, depth, path, used, results):
        if depth == len(chars):
            permutation = ''.join(path)
            if is_palindrome(permutation) and len(permutation) >= 3:
                results.add(permutation)
            return
        for i in range(len(chars)):
            if used[i]:
                continue
            if i > 0 and chars[i] == chars[i - 1] and (not used[i - 1]):
                continue
            used[i] = True
            path.append(chars[i])
            generate_permutations(chars, depth + 1, path, used, results)
            path.pop()
            used[i] = False
    if len(s) < 8:
        return set()
    substring = s[5:8].lower()
    chars = sorted((c for c in substring if c.isalpha()))
    results = set()
    generate_permutations(chars, 0, [], [False] * len(chars), results)
    return results