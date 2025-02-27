from nltk.corpus import stopwords
    from nltk import word_tokenize
    from nltk.stem import WordNetLemmatizer
    import re

def palindromes_of_specific_lengths(text):
    text = text.lower()
    text = re.sub('[^a-z0-9\\\\s]', '', text)
    text = ' '.join([x for x in word_tokenize(text) if x not in stopwords.words('english')])
    lemmatizer = WordNetLemmatizer()
    text = ' '.join([lemmatizer.lemmatize(x) for x in text.split()])
    text_list = text.split(' ')
    palindromes = set()
    for i in range(11, 87):
        for j in range(i - 4, i + 1):
            if j >= 0 and j <= len(text_list):
                palindrome = ' '.join(text_list[j:i])
                if palindrome == palindrome[::-1] and 4 <= len(palindrome) <= 5:
                    print(palindrome)
                    palindromes.add(palindrome)
    return palindromes