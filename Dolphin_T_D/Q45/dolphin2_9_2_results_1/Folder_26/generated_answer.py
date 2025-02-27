def palindromes_between_indices(s):
    sub_s = s[4:7]
    English_letters = set([c for c in 'abcdefghijklmnopqrstuvwxyz'])
    Palindromes = set()
    for word in sub_s:
        if word.lower() in English_letters:
            for i in range(len(sub_s) + 1):
                for j in range(i + 2, len(sub_s) + 1):
                    if sub_s[i:j][::-1].lower() in Palindromes:
                        Palindromes.remove(sub_s[i:j][::-1].lower())
                    else:
                        Palindromes.add(sub_s[i:j][::-1].lower())
    return Palindromes