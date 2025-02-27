from collections import defaultdict

def palindrome_of_length_n(text):
    text = text.lower()
    dict_store_string = defaultdict(list)
    palindrome_in_text = set()
    for word in text.split():
        new_word = ''.join([i for i in word if i.isalpha()])
        dict_store_string[len(new_word)].append(new_word)
    for i in dict_store_string[59]:
        palindrome_in_text.add(i)
    return palindrome_in_text