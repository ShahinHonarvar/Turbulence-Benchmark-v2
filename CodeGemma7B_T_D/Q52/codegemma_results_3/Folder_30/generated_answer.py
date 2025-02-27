def palindrome_of_length_n(text):
    pali = set()
    for i in range(len(text) - 93):
        k = 94
        while k > 0:
            t = text[i:i + k]
            if t == t[::-1]:
                pali.add(t)
            k -= 1
    return pali