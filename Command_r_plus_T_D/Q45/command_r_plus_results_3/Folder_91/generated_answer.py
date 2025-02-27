def palindromes_between_indices(s: str) -> set:
    english_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    filtered_string = ''.join(filter(english_letters.__contains__, s[2:7]))
    unique_letters = set(filtered_string)
    palindromes = set()
    for letter in unique_letters:
        if filtered_string.count(letter) % 2 == 0:
            palindromes.add(letter)
        else:
            return set()
    return palindromes