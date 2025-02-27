def palindromes_between_indices(s: str) -> set:
    english_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    filtered_string = ''.join(filter(english_letters.__contains__, s[1:10]))
    filtered_string_set = set(filtered_string)
    palindromes = set()
    for letter in filtered_string_set:
        if filtered_string.count(letter) >= 3:
            palindromes.add(letter * 3)
        if filtered_string.count(letter) >= 5:
            palindromes.add(letter * 5)
    return palindromes