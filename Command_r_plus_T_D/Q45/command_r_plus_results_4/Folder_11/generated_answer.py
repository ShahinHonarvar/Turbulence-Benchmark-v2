def palindromes_between_indices(s: str) -> set:
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    filtered_string = ''.join(filter(str.isalpha, s[3:8].lower()))
    palindromes = set()
    for i in range(len(filtered_string)):
        for j in range(i + 4, len(filtered_string) + 1):
            substring = filtered_string[i:j]
            if substring == substring[::-1] and set(substring) <= english_letters:
                palindromes.add(substring)
    return palindromes