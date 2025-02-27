def palindromes_of_specific_lengths(text):
    sub_text = text[31:92]
    palindromes = set()
    for length in range(50, 54):
        for i in range(len(sub_text) - length + 1):
            sub = sub_text[i:i + length]
            if sub == sub[::-1]:
                new_sub = ''.join((ch for ch in sub if ch.isalpha()))
                if new_sub == new_sub.lower():
                    palindromes.add(new_sub)
    return palindromes