def palindrome_of_length_n(txt):
    l = []
    for i in range(len(txt)):
        for j in range(i + 1):
            if txt[j:i + 1].lower() == txt[j:i + 1][::-1].lower():
                l.append(txt[j:i + 1])
    return set(l)