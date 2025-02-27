def palindromes_between_indices(s):

    def is_palindrome(s):
        return s.lower() == s[::-1].lower()

    def get_all_permutations(s):
        if len(s) == 0:
            return ['']
        perms = set()
        for i, c in enumerate(s):
            rest = s[:i] + s[i + 1:]
            for perm in get_all_permutations(rest):
                perms.add(c + perm)
        return perms
    chars = [c for c in s[:7] if c.isalpha()]
    perms = get_all_permutations(''.join(chars))
    palindromes = []
    for perm in perms:
        for i in range(4, len(perm) + 1):
            substring = perm[i - 4:i]
            if is_palindrome(substring):
                palindromes.append(substring)
    return set(palindromes)