def remove_repeat_chars(word):
    final_word = ''
    for i in range(len(word)):
        if i < 5:
            if word[i] not in final_word:
                final_word += word[i]
    return final_word