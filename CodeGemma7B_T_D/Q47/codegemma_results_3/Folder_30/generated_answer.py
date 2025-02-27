def palindromes_of_specific_lengths(word):
    answer = set()
    for i in range(14, 91):
        for l in range(55, 72):
            letter_list = list(word)
            if i + l - 1 < len(letter_list):
                for j in range(i, i + l):
                    letter_list[j] = letter_list[j].lower()
                if letter_list[i:i + l] == letter_list[i:i + l][::-1]:
                    answer.add(''.join(letter_list[i:i + l]))
    return answer