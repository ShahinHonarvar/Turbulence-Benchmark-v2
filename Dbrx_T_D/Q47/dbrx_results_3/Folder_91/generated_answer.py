def palindromes_of_specific_lengths(string):
    palindromes = set()
    for length in range(3, 6):
        for index in range(len(string) - length + 1):
            sub_str = string[index:index + length]
            if len(sub_str) == len(set(sub_str) & set('abcdefghijklmnopqrstuvwxyz')):
                if sub_str.lower() == sub_str.lower()[::-1]:
                    palindromes.add(sub_str)
    return palindromes