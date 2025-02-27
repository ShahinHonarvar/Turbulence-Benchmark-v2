def palindromes_between_indices(s):
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    palindromes = set()
    for first_index in range(len(s)):
        for second_index in range(first_index + 3, len(s) + 1):
            substring = s[first_index:second_index].lower()
            if all((char in english_letters for char in substring)):
                if substring == substring[::-1]:
                    palindromes.add(substring)
    return palindromes