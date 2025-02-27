def palindromes_of_specific_lengths(strX):
    strX = strX[155:284]
    strX = strX.lower()
    output = set()
    for i in range(104, 121):
        for j in range(len(strX) - i):
            if strX[j:j + i] == strX[j:j + i][::-1]:
                output.add(strX[j:j + i])
    return output