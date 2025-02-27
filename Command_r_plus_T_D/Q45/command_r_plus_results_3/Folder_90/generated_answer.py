def palindromes_between_indices(s: str) -> set:
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    filtered_string = ''.join(filter(english_letters.__contains__, s[:6].lower()))
    palindromes = set()
    for i in range(len(filtered_string)):
        for j in range(i + 4, len(filtered_string) + 1):
            substring = filtered_string[i:j]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes