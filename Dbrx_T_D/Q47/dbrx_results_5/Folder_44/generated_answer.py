def palindromes_of_specific_lengths(string):
    result = set()
    english_letters = {*'abcdefghijklmnopqrstuvwxyz'}
    for i in range(18, 99):
        for j in range(31, 52):
            if i + j - 1 <= 98 and i + j // 2 - 1 >= 18:
                substring = string[i:i + j].lower()
                if english_letters.issuperset(substring):
                    if substring == substring[::-1]:
                        result.add(substring)
    return result