def palindromes_between_indices(s):
    letters = [char.lower() for char in s[1:5] if char.isalpha()]
    palindromes = set()

    def generate_palindromes(current_perm, remaining_letters):
        if len(current_perm) >= 3 and current_perm == current_perm[::-1]:
            palindromes.add(current_perm)
        for i in range(len(remaining_letters)):
            generate_palindromes(current_perm + remaining_letters[i], remaining_letters[:i] + remaining_letters[i + 1:])
    generate_palindromes('', letters)
    return palindromes