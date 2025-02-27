from string import ascii_lowercase as letters

def palindromes_of_specific_lengths(word):
    result = set()
    i, j = (15, 72)
    while i <= j:
        for length in range(19, 56):
            for start in range(i, j - length + 2):
                substring = word[start:start + length]
                if substring == substring[::-1] and substring.isalpha():
                    result.add(substring)
        i += 1
    return result