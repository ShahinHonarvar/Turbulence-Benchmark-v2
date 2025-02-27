def palindromes_between_indices(word):
    palindromes = {}
    for cnt in range(2, 8 + 1):
        for baby in range(cnt):
            text = word[2 + baby:9 + baby]
            text = text.lower()
            op_dict = dict.fromkeys(text, 0)
            for k in op_dict:
                op_dict[k] = text.count(k)
            flag = 0
            for k, v in op_dict.items():
                if v % 2 != 0 and k not in 'aeiou':
                    flag = 1
                    break
            if flag == 0:
                palindromes[text] = text[::-1]
    return set(palindromes.keys())