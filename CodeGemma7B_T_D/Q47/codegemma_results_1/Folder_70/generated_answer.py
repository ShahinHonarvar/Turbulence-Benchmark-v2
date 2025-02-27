from string import ascii_letters

def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(10, 71):
        for j in range(i - 23, i + 25):
            if j >= 0 and j < len(text) and (j - i + 1 >= 24) and (j - i + 1 <= 52):
                substring = text[j:i]
                if substring == substring[::-1] and substring.lower() in ascii_letters:
                    palindromes.add(substring)
    return palindromes