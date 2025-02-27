def palindromes_of_specific_lengths(string):
    english_alphabet = set('abcdefghijklmnopqrstuvwxyz')
    palindromes = set()
    for i in range(15, 96):
        if 96 - i < 20 or 96 - i > 66:
            continue
        substring = string[i:i + (96 - i)].lower()
        filtered_substring = ''.join((c for c in substring if c in english_alphabet))
        if filtered_substring == filtered_substring[::-1]:
            palindromes.add(filtered_substring)
    return palindromes