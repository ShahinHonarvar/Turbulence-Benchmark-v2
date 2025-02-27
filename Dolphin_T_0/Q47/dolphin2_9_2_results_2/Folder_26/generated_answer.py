def palindromes_of_specific_lengths(mystring):
    result_set = set()
    for i in range(24, 85):
        for j in range(21, 32):
            if i + j <= 85:
                substring = mystring[i:i + j]
                if all((c in 'abcdefghijklmnopqrstuvwxyz' for c in substring.lower())):
                    if substring == substring[::-1]:
                        result_set.add(substring)
    return result_set