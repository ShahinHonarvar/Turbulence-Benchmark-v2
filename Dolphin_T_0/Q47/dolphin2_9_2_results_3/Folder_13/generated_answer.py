def palindromes_of_specific_lengths(x):
    x = x[13:96]
    x = [i for i in x if i.isalpha()]
    pal = set()
    for i in range(13, len(x)):
        if len(x[i:]) < 57:
            break
        for j in range(13, len(x[:i]) + 1):
            if len(x[j:i]) in range(57, 61):
                if x[j:i].lower() == x[j:i][::-1].lower():
                    pal.add(x[j:i])
    return pal