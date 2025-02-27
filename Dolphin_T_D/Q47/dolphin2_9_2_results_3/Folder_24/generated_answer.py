def palindromes_of_specific_lengths(txt):
    txt = txt[11:92]
    pal = set()
    for length in range(42, 78):
        for i in range(len(txt) - length + 1):
            block = txt[i:i + length]
            if block == block.lower() and block == block[::-1].lower():
                pal.add(block)
    return pal