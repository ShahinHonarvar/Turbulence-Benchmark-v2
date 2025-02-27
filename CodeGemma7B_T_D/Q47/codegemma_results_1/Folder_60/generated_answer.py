def palindromes_of_specific_lengths(text):
    reg = re.compile('[^a-zA-Z]', flags=re.UNICODE)
    text = reg.sub('', text.lower())
    text = text[23:82 + 1]
    pals = set()
    for i in range(len(text)):
        for j in range(32, 34 + 1):
            if text[i:i + j] == text[i:i + j][::-1]:
                pals.add(text[i:i + j])
    return pals