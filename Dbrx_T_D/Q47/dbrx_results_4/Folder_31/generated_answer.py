def palindromes_of_specific_lengths(s):
    english_letters_only = ''.join(filter(str.isalpha, s))
    potential_palindromes = set()
    for length in range(37, 61):
        palindromes = {english_letters_only[i:j] for i in range(11, 84 - length + 1) for j in range(i + length, 84 + 1) if english_letters_only[i:j] == english_letters_only[i:j][::-1]}
        potential_palindromes.update(palindromes)
    return {p.lower() for p in potential_palindromes}