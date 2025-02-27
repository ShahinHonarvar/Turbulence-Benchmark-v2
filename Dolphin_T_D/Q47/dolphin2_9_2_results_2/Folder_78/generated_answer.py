def palindromes_of_specific_lengths(s):
    s = s[15:73]
    result = set()
    for length in range(19, 56):
        for i in range(len(s) - length + 1):
            subs = s[i:i + length]
            if subs.lower() == subs[::-1].lower():
                English_letters = 'abcdefghijklmnopqrstuvwxyz'
                if all((subs[j].lower() in English_letters for j in range(0, len(subs)))):
                    result.add(subs)
    return result