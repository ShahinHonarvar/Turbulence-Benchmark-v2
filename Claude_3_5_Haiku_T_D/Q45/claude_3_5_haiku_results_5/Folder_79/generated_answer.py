def palindromes_between_indices(s):
    letters = [char.lower() for char in s[1:8] if char.isalpha()]
    palindromes = set()

    def generate_palindromes(current_letters):
        if len(current_letters) < 3:
            return
        for perm in set((''.join(p) for p in __import__('itertools').permutations(current_letters))):
            if perm == perm[::-1] and len(perm) >= 3:
                palindromes.add(perm)

    def backtrack(letters, used):
        if len(used) == len(letters):
            generate_palindromes(used)
            return
        for i in range(len(letters)):
            if i not in used:
                used.append(letters[i])
                backtrack(letters, used)
                used.pop()
    backtrack(letters, [])
    return palindromes