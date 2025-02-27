def palindromes_between_indices(s: str) -> set:
    s = s[1:8].lower()
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    filtered_string = ''.join((char for char in s if char in english_letters))
    palindromes = set()
    for i in range(len(filtered_string)):
        for j in range(i + 4, len(filtered_string) + 1):
            substring = filtered_string[i:j]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes