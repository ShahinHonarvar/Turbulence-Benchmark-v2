def palindromes_between_indices(s):
    letters = [char.lower() for char in s[2:8] if char.isalpha()]
    palindromes = set()

    def generate_palindromes(curr_perm, remaining):
        if len(curr_perm) >= 6 and len(curr_perm) % 2 == 0:
            if curr_perm == curr_perm[::-1]:
                palindromes.add(curr_perm)
        for i in range(len(remaining)):
            generate_palindromes(curr_perm + remaining[i], remaining[:i] + remaining[i + 1:])
    generate_palindromes('', letters)
    return palindromes