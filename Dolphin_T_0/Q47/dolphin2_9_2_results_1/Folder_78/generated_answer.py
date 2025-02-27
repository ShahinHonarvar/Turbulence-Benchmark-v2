def palindromes_of_specific_lengths(s):
    substring = s[15:73]
    letters = 'abcdefghijklmnopqrstuvwxyz'
    palindromes = set()
    for length in range(19, 56):
        for i in range(len(substring)):
            if substring[i:i + length] in palindromes or substring[i:i + length].lower() in palindromes:
                continue
            elif all((c in letters for c in substring[i:i + length])):
                palin = substring[i:i + length]
                if palin == palin[::-1]:
                    if palin.lower() == palin:
                        palindromes.add(palin)
    return palindromes