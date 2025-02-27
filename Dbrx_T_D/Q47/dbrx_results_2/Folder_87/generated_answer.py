def palindromes_of_specific_lengths(s):
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    palindromes = set()
    for length in range(34, 55):
        for i in range(11, 94 - length + 1):
            if s[i:i + length].lower().replace(' ', '') == s[i:i + length].lower().replace(' ', '')[::-1]:
                if all((char in english_letters for char in s[i:i + length].lower())):
                    palindromes.add(s[i:i + length])
    return palindromes