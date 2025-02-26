def palindromes_between_indices(s):
    letters = [char.lower() for char in s[1:6] if char.isalpha()]
    palindromes = set()

    def backtrack(current_perm, unused_letters):
        if len(current_perm) >= 6 and current_perm == current_perm[::-1]:
            palindromes.add(current_perm)
        for i in range(len(unused_letters)):
            next_perm = current_perm + unused_letters[i]
            next_unused = unused_letters[:i] + unused_letters[i + 1:]
            backtrack(next_perm, next_unused)
    backtrack('', letters)
    return palindromes