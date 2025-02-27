def palindromes_of_specific_lengths(test):
    set(filter(lambda x: x.lower() in test[33:86] and len(x) in range(26, 32) and (x == x[::-1]), map(str, filter(str.isalpha, test))))