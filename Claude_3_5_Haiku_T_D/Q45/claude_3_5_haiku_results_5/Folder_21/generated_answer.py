def palindromes_between_indices(s):
    letters = [char.lower() for char in s[1:9] if char.isalpha()]
    palins = set()

    def generate_palindromes(curr_letters, current_palin):
        if len(current_palin) >= 7 and len(current_palin) % 2 == 1:
            if current_palin == current_palin[::-1]:
                palins.add(current_palin)
        for i in range(len(curr_letters)):
            next_letters = curr_letters[:i] + curr_letters[i + 1:]
            generate_palindromes(next_letters, current_palin + curr_letters[i])
    generate_palindromes(letters, '')
    return palins