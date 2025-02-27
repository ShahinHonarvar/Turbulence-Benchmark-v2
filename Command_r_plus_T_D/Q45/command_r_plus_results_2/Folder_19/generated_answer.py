def palindromes_between_indices(s: str) -> set:
    english_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    filtered_string = ''.join(filter(english_letters.__contains__, s[1:8]))
    palindromes = set()
    if len(filtered_string) >= 7:
        for i in range(len(filtered_string) - 6):
            substring = filtered_string[i:i + 7]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes