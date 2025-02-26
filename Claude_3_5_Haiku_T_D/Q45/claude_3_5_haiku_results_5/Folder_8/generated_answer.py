def palindromes_between_indices(s):
    letters = [char.lower() for char in s[1:6] if char.isalpha()]
    palindromes = set()

    def generate_palindromes(current_perm, remaining):
        if len(current_perm) >= 5 and current_perm == current_perm[::-1]:
            palindromes.add(current_perm)
        for i in range(len(remaining)):
            generate_palindromes(current_perm + remaining[i], remaining[:i] + remaining[i + 1:])
    generate_palindromes('', letters)
    return palindromes